import React from 'react';
import ReactDOM from 'react-dom';
import FocusTrapReact from 'focus-trap-react';

const App = () => {
  return (
    <FocusTrapReact>
      <div>
        <h1>2020 Black</h1>
        <p>This is online shop.</p>
        <button>Lets go shopping !</button>
      </div>
    </FocusTrapReact>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));