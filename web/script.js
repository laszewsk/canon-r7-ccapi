// Onclick of the button
document.querySelector("button").onclick = function () {
  // Call python's random_python function
  eel.random_python()(function(number){
    // Update the div with a random number returned by python
    document.querySelector(".random_number").innerHTML = number;
  })
}