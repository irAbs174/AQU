$(document).ready(function() {
  $("#support_log").html("");
  let currentPath = window.location.pathname;
  let user_phoneNumber = currentPath.split('/').filter(Boolean).pop();
  $.getJSON(`/api/support/?search=${user_phoneNumber}`, function(message_data){
      for(let i = 0; i <= message_data.count; i++){
          message = message_data.results[i];
          $("#USER_PHONE").html(`<h3 id="USER_PHONE" class="m-b-0">${user_phoneNumber}</h3>`);
          $("input[name=PHONE_HIDDEN]").val(`${user_phoneNumber}`);
          if(message.support_status == 'USER'){
            const newMessage = $('<div>').addClass('dirltruser').append(
              $('<div>').addClass('textuser').append(
                $('<p>').text(message.message),
                $('<span>').addClass('time-right').text(message.time)
              )
            );
            $("#support_log").append(newMessage);
          }else{
            const newMessage = $('<div>').addClass('dirrtladmin').append(
              $('<div>').addClass('textadmin darker').append(
                $('<p>').text(message.message),
                $('<span>').addClass('time-right').text(message.time)
              )
            );
            $("#support_log").append(newMessage);
          };// End if SUPPORT_STATUS
      }// END for i
      fetchLatestMessages();
  }) // End getJSON message_data
});//End ready
// JavaScript (support.js)
const messageInputDom = document.querySelector('#support_message');
const submitButtonDom = document.querySelector('#support_submit');
const token = $('input[name=csrfmiddlewaretoken]').val();

// Create a new Date object {
var date = new Date();
// Get the current hour and minute
var hours = date.getHours();
var minutes = date.getMinutes();
// Format the hour and minute to have leading zeros if necessary
hours = (hours < 10 ? "0" : "") + hours;
minutes = (minutes < 10 ? "0" : "") + minutes;
// Create the time string in the desired format
var time = hours + ":" + minutes;
//

// Focus on the message input field when the page loads
messageInputDom.focus();

// Handle enter key press on the message input field
messageInputDom.addEventListener('keyup', function(e) {
  if (e.keyCode === 13) {  // Enter key pressed
    submitButtonDom.click();
  }
});

// Handle submit button click
submitButtonDom.addEventListener('click', function(e) {
  let currentPath = window.location.pathname;
  let slug = currentPath.split('/').filter(Boolean).pop();
  const message = messageInputDom.value;
  if (message) {
    const support_status = "active";
    const data = {
      'support_room': slug,
      'support_message': message,
      'support_status': support_status,
      'time': time,
      'csrfmiddlewaretoken': token,
    };
    $.ajax({
      url: '/support/post_message', 
      type: 'POST',
      data: data,
      success: function(response) {
        if (response.success === false) {
          Swal.fire({
            icon: "error",
            title: response.status,
            showConfirmButton: false,
            timer: 3000,
          });
        } else {
          // Handle success case if needed
          // Clear the message input field after successful submission
          messageInputDom.value = '';
        }
      },
      error: function(xhr, status, error) {
        Swal.fire({
          icon: "error",
          title: status,
          showConfirmButton: false,
          timer: 3000,
        });
      }
    });
  } else {
    Swal.fire({
      icon: "error",
      title: "پیام پشتیبانی نمیتواند خالی باشد",
      showConfirmButton: false,
      timer: 2000,
    });
  }
});

// Function to poll for new messages
function pollMessages(timestamp) {
  let currentPath = window.location.pathname;
  let slug = currentPath.split('/').filter(Boolean).pop();
  $.ajax({
    url: '/support/get_message',
    data: { 'timestamp': timestamp, 'support_room': slug },
    success: function(data) {
      const messages = data.messages;
      for (const message of messages) {
        console.log(message.time)
        if(message.status == 'USER'){
          const newMessage = $('<div>').addClass('dirltruser').append(
            $('<div>').addClass('textuser').append(
              $('<p>').text(message.message),
              $('<span>').addClass('time-right').text(message.time)
            )
          );
          $("#support_log").append(newMessage);
        }else{
          const newMessage = $('<div>').addClass('dirrtladmin').append(
            $('<div>').addClass('textadmin darker').append(
              $('<p>').text(message.message),
              $('<span>').addClass('time-right').text(message.time)
            )
          );
          $("#support_log").append(newMessage);
        }
      }
      if (messages.length > 0) {
        const lastTimestamp = messages[messages.length - 1].timestamp;
        pollMessages(lastTimestamp);
      } else {
        // Adjust the polling interval to your preference
        setTimeout(function() {
          pollMessages(timestamp);
        }, 2000);
      }
    },
    error: function(xhr, status, error) {
      // Adjust the polling interval to your preference
      setTimeout(function() {
        pollMessages(timestamp);
      }, 2000);
    },
    timeout: 30000,
    dataType: 'json'
  });
}

// Initial function to fetch latest messages and start long polling
function fetchLatestMessages() {
  let search_user = $('input[name=Supported_user]').val();
  $.ajax({
    url: `/api/support/?search=${search_user}`,
    type: 'GET',
    dataType: 'json',
    success: function(response) {
      var results = response.results;
      if (results.length > 0) {
        let support_timestamp = results[results.length - 1].timestamp;
        pollMessages(support_timestamp);
      } else {
        // Adjust the polling interval to your preference
        setTimeout(fetchLatestMessages, 2000);
      }
    },
    error: function(xhr, status, error) {
      // Adjust the polling interval to your preference
      setTimeout(fetchLatestMessages, 2000);
    }
  });
}

fetchLatestMessages();
