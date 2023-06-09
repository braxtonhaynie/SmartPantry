def Get_html(IP, PORT):
    html = '''
<!DOCTYPE HTML>
<html>

<head>
    <title>Smart Pantry</title>
    <style>
      html { 
        font-family: Helvetica; 
        display: inline-block; 
        margin: 0px; 
        text-align: center;
      }

      body{
          margin: 0px;
      }

      .header {
          padding: 1px;
          padding-left: 50px;
          text-align: left;
          background: #FF8200;
          color: #FF8200;
          font-size: 30px;
      }

      .container {
          width: 100%;
          height: 100vh;
          display: table;
      }

      .leftpane {
          width: 65%;
          height: 100%;
          float: left;
      }

      .rightpane {
          float: left;
          width: 35%;
          height: 100%;
      }

      @media only screen and (max-width: 1000px) {
          .leftpane, .rightpane {
            width: 100%;
            height: 75%;
          }
      }

      h1 {
          color: #444444;
          font-size: 120%;
      }

      h2 {
          color: #d4d4d4;
          font-size: 1.5em;
      }

      h3 {
          color: #444444; 
          margin-bottom: 50px;
      }

      p {
          font-size: 14px;
          color: #888;
      }

      img {
          background-color: #c66b0a;
          width : 95%;
          height: auto;
          display: block;
          margin: auto;
          -webkit-transform: rotate(180deg);
          -moz-transform: rotate(180deg);
          -ms-transform: rotate(180deg);
          -o-transform: rotate(180deg);
          transform: rotate(180deg);
      }

      .button {
        border: none; 
        color: gray; 
        height: 15%; 
        width: 85%;
        text-align: center; 
        text-decoration: none;
        align-items: center;
        font-size: 1em;
        cursor: pointer;
        border-radius: 20px;
        margin-bottom: 10px;
        display: block;
      }

      .button:disabled { 
          color: white;
          pointer-events: none;
          opacity: 0.3;
      }

      .button:hover { 
          background-color: #FF8200; 
          color: white;
      }

      .button:active {
          background-color: #c66b0a; 
          box-shadow: 0 5px #c66b0a; 
          transform: translateY(4px);
      }

      .selected {
          background-color: #FF8200; 
          box-shadow: 0 5px #c66b0a; 
          transform: translateY(4px);
      }

      .running {
          background-color: #f4776e;
          color: white;
          
      }

      .running:hover {
          background-color: #f44336;
          color: white;
          
      }

      .not-running {
          background-color: #5dd32f;
          color: white;
      }

      .not-running:hover {
          background-color: #6cf436;
          color: white;
      }

      .grocery-list {
          margin: auto;
          background-color: #58595B;
          text-align: center;
          border-radius: 20px;
          height: 75%;
          width: 80%;
      }

      .live-feed-window {
          margin: 0 auto;
          background-color: #58595B;
          text-align: center;
          border-radius: 20px;
          height: 75%;
          width: 95%;
      }

      .live-feed {
          width: 75%;
          height: 90%;
          float: left;
          display: flex;
      }

      .button-panel {
          width: 25%;
          height: 90%;
          float: left;
          display: flex;
          justify-content: center;
          align-items: center;
          flex-direction: column;
      }

      /* Include the padding and border in an element's total width and height */
      * {
          box-sizing: border-box;
      }

      /* Remove margins and padding from the list */
      ul {
          margin: auto;
          width: 60%;
          max-height: 35vh;
          padding: 10px;
          border-radius: 20px;
          overflow-y: scroll;
      }

      /* Style the list items */
      ul li {
          border-radius: 10px;
          margin-bottom: 5px;
          cursor: pointer;
          position: relative;
          padding: 12px 8px 10px 40px;
          list-style-type: none;
          background: #eee;
          font-size: 1em;
          transition: 0.2s;
          text-align: left;

          /* make the list items unselectable */
          -webkit-user-select: none;
          -moz-user-select: none;
          -ms-user-select: none;
          user-select: none;
      }

      /* Set all odd list items to a different color (zebra-stripes) */
      ul li:nth-child(odd) {
          background: #f9f9f9;
      }

      /* Darker background-color on hover */
      ul li:hover {
          background: #ddd;
      }

      /* When clicked on, add a background color and strike out text */
      ul li.checked {
          background: #888;
          color: #fff;
          text-decoration: line-through;
      }

      /* Add a "checked" mark when clicked on */
      ul li.checked::before {
          content: '';
          position: absolute;
          border-color: #fff;
          border-style: solid;
          border-width: 0 2px 2px 0;
          top: 10px;
          left: 16px;
          transform: rotate(45deg);
          height: 15px;
          width: 7px;
      }

      /* Style the close button */
      .close {
          border-right: 10px;
          position: absolute;
          right: 0;
          top: 0;
          padding: 12px 16px 12px 16px;
          background-color: #f4776e;
      }

      .close:hover {
          background-color: #f44336;
          color: white;
      }

      /* Clear floats after the header */
      .header:after {
          content: "";
          display: table;
          clear: both;
      }

      /* Style the input */
      input {
          margin: 0;
          border: none;
          border-radius: 0;
          width: 75%;
          padding: 10px;
          float: left;
          font-size: 1em;
        }

      /* Style the "Add" button */
      .addBtn {
          padding: 10px;
          width: 25%;
          background: #d9d9d9;
          color: #555;
          float: left;
          text-align: center;
          font-size: 1em;
          cursor: pointer;
          transition: 0.3s;
          border-radius: 0;
      }

      .addBtn:hover {
          background-color: #bbb;
      }
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
</head>

<body>
    <div class="header">
        <h1>Smart Pantry</h1>
    </div>

    <div class="container">

      <div class="leftpane">

        <div class="live-feed-window">
          <h2>Pantry Live Stream</h2>
          
          <div class="live-feed">
            <img src="stream.mjpg" />
          </div>

          <div class="button-panel">
            <button id="UP" class="button button1" name="UP" value="UP">UP</button>
            <script>
              var button1 = document.getElementById("UP");
              var intervalId1;
              var xhr1;
              var selectedOption = null;
              
              function start_Up() {
                intervalId1 = setInterval(sendRequest1, 250); // val of 500 sends a request every half-second
              }
              
              function stop_Up() {
                clearInterval(intervalId1);
                xhr1.abort(); // aborts any ongoing requests
              }

              function sendRequest1() {
                xhr1 = new XMLHttpRequest();
                xhr1.open("POST", "http://''' + IP + ''':''' + str(PORT) + '''/home/up", true);
                xhr1.setRequestHeader('Content-Type', 'application/json');
                xhr1.send();
              }

              function handleOptionSelection(event) {
                if (selectedOption !== null && selectedOption === event.target && isRunning !== true) {
                  selectedOption.classList.remove("selected");
                  selectedOption = null;
                } else {
                  if (selectedOption !== null) {
                    selectedOption.classList.remove("selected");
                  }
                  selectedOption = event.target;
                  selectedOption.classList.add("selected");
                  console.log(event.target.id)
                }
              }
              button1.addEventListener("click", handleOptionSelection);
            </script>

            <button id="DOWN" class="button button2" name="DOWN" value="DOWN">DOWN</button>
            <script>
              var button2 = document.getElementById("DOWN");
              var intervalId2;
              var xhr2;
              
              function start_Down() {
                intervalId2 = setInterval(sendRequest2, 250); // val of 500 sends a request every half-second
              }
              
              function stop_Down() {
                clearInterval(intervalId2);
                xhr2.abort(); // aborts any ongoing requests
              }

              function sendRequest2() {
                xhr2 = new XMLHttpRequest();
                xhr2.open("POST", "http://''' + IP + ''':''' + str(PORT) + '''/home/down", true);
                xhr2.setRequestHeader('Content-Type', 'application/json');
                xhr2.send();
              }

			        button2.addEventListener("click", handleOptionSelection);
            </script>
            
            <button id="ST-SP" class="button button3 not-running" name="ST-SP" value="ST-SP">START</button>
            <script>
              var button3 = document.getElementById("ST-SP");
              var isRunning = false;

              button3.addEventListener("click", () => {
                if (selectedOption === null) {
                  console.log("select up or down")
                  button3.classList.remove("running");
                  button3.classList.add("not-running");
                  document.getElementById("DOWN").disabled = false;
                  document.getElementById("UP").disabled = false;
                  button3.textContent = "START";
                }
                else{
                  if (!isRunning) {
                    button3.classList.add("running");
                    button3.classList.remove("not-running");
                    button3.textContent = "STOP";
                    isRunning = true;
                    if (selectedOption.id === "UP" ) { // start up
                      console.log("UP starting");
                      document.getElementById("DOWN").disabled = true;
                      document.getElementById("UP").disabled = false;
                      start_Up();
                    }
                    else { // start down
                      console.log("Down starting");
                      document.getElementById("DOWN").disabled = false;
                      document.getElementById("UP").disabled = true;
                      start_Down();
                    }
                  }
                  else {
                    button3.classList.add("not-running");
                    button3.classList.remove("running");
                    button3.textContent = "START";
                    document.getElementById("DOWN").disabled = false;
                    document.getElementById("UP").disabled = false;
                    isRunning = false;
                    if (selectedOption.id === "UP" ) { // stop up
                      console.log("UP stopping");
                      stop_Up();
                    }
                    else { // stop down
                      console.log("Down stopping");
                      stop_Down();
                    }
                    if (selectedOption !== null) {
                      selectedOption.classList.remove("selected");
                      selectedOption = null;
                    }
                  }
                }
                
                console.log(isRunning);
              });
            </script>
          </div>
        </div> 
      </div>

      <div class="rightpane">

        <div class="grocery-list">
          <h2>Grocery List</h2>
            
          <input type="text" id="myInput" placeholder="Item">
          <span onclick="newElement()" class="addBtn">Add</span>
          
          <div style="padding-top: 75px;"> 
            <ul id="myUL">
              <li>Beans</li>
              <li class="checked">Bananas</li>
              <li>OJ</li>
              <li>Carrots</li>
              <li>Broccoli</li>
            </ul>
          </div>
        </div>

        <script>
          // Create a "close" button and append it to each list item
          var myNodelist = document.getElementsByTagName("LI");
          var i;
          for (i = 0; i < myNodelist.length; i++) {
            var span = document.createElement("SPAN");
            var txt = document.createTextNode("X");
            span.className = "close";
            span.appendChild(txt);
            myNodelist[i].appendChild(span);
          }
          
          // Click on a close button to hide the current list item
          var close = document.getElementsByClassName("close");
          var i;
          for (i = 0; i < close.length; i++) {
            close[i].onclick = function() {
              var div = this.parentElement;
              div.style.display = "none";
            }
          }
          
          // Add a "checked" symbol when clicking on a list item
          var list = document.querySelector('ul');
          list.addEventListener('click', function(ev) {
            if (ev.target.tagName === 'LI') {
              ev.target.classList.toggle('checked');
            }
          }, false);
          
          // Create a new list item when clicking on the "Add" button
          function newElement() {
            var li = document.createElement("li");
            var inputValue = document.getElementById("myInput").value;
            var t = document.createTextNode(inputValue);
            li.appendChild(t);
            if (inputValue === '') {
              alert("You must write something!");
            } else {
              document.getElementById("myUL").appendChild(li);
            }
            document.getElementById("myInput").value = "";
          
            var span = document.createElement("SPAN");
            var txt = document.createTextNode("X");
            span.className = "close";
            span.appendChild(txt);
            li.appendChild(span);
          
            for (i = 0; i < close.length; i++) {
              close[i].onclick = function() {
                var div = this.parentElement;
                div.style.display = "none";
              }
            }
          }
        </script>
      </div>
    </div>

</body>
</html>
'''
    return html