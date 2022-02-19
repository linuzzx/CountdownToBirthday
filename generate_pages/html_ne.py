html = '''
<!DOCTYPE html>
<head>
  
  <!-- ALL CREDIT GOES TO https://codepen.io/AllThingsSmitty/pen/JJavZN
   You didn't expect me to code this myself did you? -->
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
<title>Birthday Counter</title>
<style>
/* general styling */
:root {{
  --smaller: .75;
}}

* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

html, body {{
  height: 100%;
  margin: 0;
}}

body {{
  align-items: center;
  background-color: {bg};
  display: flex;
  font-family: -apple-system, 
    BlinkMacSystemFont, 
    "Segoe UI", 
    Roboto, 
    Oxygen-Sans, 
    Ubuntu, 
    Cantarell, 
    "Helvetica Neue", 
    sans-serif;
}}

.container {{
  color: #333;
  margin: 0 auto;
  text-align: center;
}}

h1 {{
  font-weight: normal;
  letter-spacing: .125rem;
  text-transform: uppercase;
}}

li {{
  display: inline-block;
  font-size: 1.5em;
  list-style-type: none;
  padding: 1em;
  text-transform: uppercase;
}}

li span {{
  display: block;
  font-size: 4.5rem;
}}

.emoji {{
  display: none;
  padding: 1rem;
}}

.emoji span {{
  font-size: 4rem;
  padding: 0 .5rem;
}}

@media all and (max-width: 768px) {{
  h1 {{
    font-size: calc(1.5rem * var(--smaller));
  }}
  
  li {{
    font-size: calc(1.125rem * var(--smaller));
  }}
  
  li span {{
    font-size: calc(3.375rem * var(--smaller));
  }}
}}
</style>
</head>

<body>
    <div class="container">
        <h1 id="headline">Countdown to my birthday</h1>
        <div id="countdown">
          <ul>
            <li><span id="days"></span>days</li>
            <li><span id="hours"></span>Hours</li>
            <li><span id="minutes"></span>Minutes</li>
            <li><span id="seconds"></span>Seconds</li>
          </ul>
        </div>
        <div id="content" class="emoji">
          <span>Happy Birthday!</span>
        </div>
      </div>
<script type="text/javascript">
(function () {{
  const second = 1000,
    minute = second * 60,
    hour = minute * 60,
    day = hour * 24;

  //I'm adding this section so I don't have to keep updating this pen every year :-)
  //remove this if you don't need it
  let today = new Date(),
    dd = String(today.getDate()).padStart(2, "0"),
    mm = String(today.getMonth() + 1).padStart(2, "0"),
    yyyy = today.getFullYear(),
    nextYear = yyyy + 1,
    dayMonth = "{month}/{day}/",
    birthday = dayMonth + yyyy;

  today = mm + "/" + dd + "/" + yyyy;
  if (today > birthday) {{
    birthday = dayMonth + nextYear;
  }}
  //end

  const countDown = new Date(birthday).getTime(),
    x = setInterval(function () {{
      const now = new Date().getTime(),
        distance = countDown - now;

      (document.getElementById("days").innerText = Math.floor(distance / day)),
        (document.getElementById("hours").innerText = Math.floor(
          (distance % day) / hour
        )),
        (document.getElementById("minutes").innerText = Math.floor(
          (distance % hour) / minute
        )),
        (document.getElementById("seconds").innerText = Math.floor(
          (distance % minute) / second
        ));

      //do something later when date is reached
      if (distance < 0) {{
        document.getElementById("headline").innerText = "";
        document.getElementById("countdown").style.display = "none";
        document.getElementById("content").style.display = "block";
        clearInterval(x);
      }}
      //seconds
    }}, 0);
}})();

</script>
</body>
</html>
'''