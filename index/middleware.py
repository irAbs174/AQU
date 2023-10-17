from django.utils.deprecation import MiddlewareMixin
from django.contrib.sessions.models import Session
from datetime import datetime, timedelta
from django.conf import settings
from user_agents import parse
from .models import Visit
import geoip2.database


class OnlineVisitorsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Retrieve session keys from the cache
        session_keys = settings.CACHE.get('online_users', [])

        # Retrieve active sessions from the database
        sessions = Session.objects.filter(session_key__in=session_keys)

        # Filter active sessions based on last activity time
        active_sessions = []
        for session in sessions:
            last_activity = session.get_decoded().get('_session_expiry')
            if last_activity and last_activity + timedelta(seconds=settings.ONLINE_USERS_TIMEOUT) > datetime.now():
                active_sessions.append(session.session_key)

        # Update the session keys in the cache
        settings.CACHE.set('online_users', active_sessions, settings.ONLINE_USERS_TIMEOUT)


class UniqueVisitsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        session_key = request.session.session_key

        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        visit, created = Visit.objects.get_or_create(session_key=session_key)
        visit.increment_visit_count()
        visit.last_visit_url = request.path

        # Capture IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        visit.ip_address = ip

        # Capture user agent details
        user_agent = parse(request.META.get('HTTP_USER_AGENT', ''))
        visit.browser = user_agent.browser.family
        visit.browser_version = user_agent.browser.version_string
        visit.os = user_agent.os.family
        visit.os_version = user_agent.os.version_string
        visit.device = user_agent.device.family

        # Save the visit instance
        visit.save()
        request.visit = visit