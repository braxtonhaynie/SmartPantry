def Get_html(IP, PORT):
    html = '''
<!DOCTYPE HTML>
<html>

<head>
    <title>Smart Pantry</title>
    <link rel="stylesheet" href="styles.css">
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
        }

        .leftpane {
            width: 65%;
            height: 100vh;
        }

        .rightpane {
            width: 35%;
            height: 100vh;
        }

        .d-flex {
            display: flex;
        }

        h1 {
            color: #444444;
        }

        h2 {
            color: #d4d4d4;
        }

        h3 {
            color: #444444; 
            margin-bottom: 50px;
        }

        p {
            font-size: 14px;
            color: #888;
            margin-bottom: 10px;
        }

        .button { 
            border: none; 
            color: gray; 
            height: 150px; 
            width: 150px; 
            text-align: center; 
            text-decoration: none; 
            display: inline-block; 
            font-size: 16px; 
            margin: 4px 2px; 
            cursor: pointer; 
            border-radius: 50px;
        }

        .button:hover { 
            background-color: #FF8200; 
            color: white;
        }

        .button:active {
            background-color: #c66b0a; 
            box-shadow: 0 5px #666; 
            transform: translateY(4px);
        }

        .row {
            display: flex;
            flex-direction:row;
        }

        .column {
            flex: 1 1 0px;
        }

        .column-member {
            display: flex;
            text-align: center;
        }

        .grocery-list {
            background-color: #58595B;
            padding: 10px;
            text-align: center;
            border-radius: 20px;
            height: 600px;
            width: 400px;
        }

        .live-feed-window {
            margin: auto;
            background-color: #58595B;
            padding: 10px;
            text-align: center;
            border-radius: 20px;
            height: 600px;
            width: 80%;
        }

        .live-feed {
            width: 75%;
            float: left;
            /* height: 100vh; */
        }

        .button-panel {
            width: 25%;
            float: left;
            /* height: 100vh; */
        }

        /* Include the padding and border in an element's total width and height */
        * {
            box-sizing: border-box;
        }

        /* Remove margins and padding from the list */
        ul {
            margin: auto;
            height: 300px;
            width: 60%;
            padding: 10px;
            border-radius: 20px;
            overflow: hidden;
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
            font-size: 18px;
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
            font-size: 16px;
        }

        /* Style the "Add" button */
        .addBtn {
            padding: 10px;
            width: 25%;
            background: #d9d9d9;
            color: #555;
            float: left;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s;
            border-radius: 0;
        }

        .addBtn:hover {
            background-color: #bbb;
        }
    
    </style
    <meta name="viewport" content="width=device-width, initial-scale=1" />
</head>

<body>
    <div class="header">
        <h1>Smart Pantry</h1>
    </div>

    <div class="container">
      <div class="d-flex">

        <div class="leftpane">
          <br>

          <div class="live-feed-window">
            <h2>Pantry Live Stream</h2>
            
            <div class="live-feed">
              <img src="stream.mjpg" width="640" height="480"/>
            </div>

            <div class="button-panel">
              <br>
              <br>
              <br>

              <button id="UP" class="button button1" name="UP" value="UP">UP</button>
              <script>
                var button1 = document.getElementById("UP");
                var intervalId1;
                var xhr1;
                
                button1.addEventListener("mousedown", function() {
                  intervalId1 = setInterval(sendRequest1, 250); // val of 500 sends a request every half-second
                });
                
                button1.addEventListener("mouseup", function() {
                  clearInterval(intervalId1);
                  xhr1.abort(); // aborts any ongoing requests
                });
                
                function sendRequest1() {
                  xhr1 = new XMLHttpRequest();
                  xhr1.open("POST", "http://''' + IP + ''':''' + str(PORT) + '''/home/up", true);
                  xhr1.setRequestHeader('Content-Type', 'application/json');
                  xhr1.send();
                }
              </script>

              <br>
              <br>
              <br>

              <button id="DOWN" class="button button2" name="DOWN" value="DOWN">DOWN</button>
              <script>
                var button2 = document.getElementById("DOWN");
                var intervalId2;
                var xhr2;
                
                button2.addEventListener("mousedown", function() {
                  intervalId2 = setInterval(sendRequest2, 250); // val of 500 sends a request every half-second
                });
                
                button2.addEventListener("mouseup", function() {
                  clearInterval(intervalId2);
                  xhr2.abort(); // aborts any ongoing requests
                });
                
                function sendRequest2() {
                  xhr2 = new XMLHttpRequest();
                  xhr2.open("POST", "http://''' + IP + ''':''' + str(PORT) + '''/home/down", true);
                  xhr2.setRequestHeader('Content-Type', 'application/json');
                  xhr2.send();
                }
              </script>
            </div>
          </div>
        </div>

        <div class="rightpane">
          <br>

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
              //var txt = document.createTextNode("\u00D7");
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
              //var txt = document.createTextNode("\u00D7");
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
    </div>

</body>
</html>
'''
    return html