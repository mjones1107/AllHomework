//Javascript Homework
// from data.js
var tableData = data;


// Select the submit button
var submit = d3.select("#submit");

// initialize form input global variable
var forminput = "";

//filter function for date according to forminput
function filterdate(ldata) {
  return ldata.date === forminput;
}
// Complete the click handler for the form
submit.on("click", function() {
  
  //prevent refresh
  d3.event.preventDefault();

  var inputElement = d3.select("#datetime");

  //read the form input
  var actualFormInput = inputElement.property("value");
  
  //set equal to global variable form input
  forminput = actualFormInput;

  //filter according to date - used filter date function

  var eventMatches = tableData.filter(filterdate);

  //Obtain an array/list of only the dates from the eventMatches array of objects
  var allDates = eventMatches.map(tableData=>tableData.datetime);
/*
  var mean = math.mean(allAges);
  var median = math.median(allAges);
  var mode = math.mode(allAges);
  var variance= math.var(allAges);
  var stddev= math.std(allAges);

  
  var inside = d3.select("ul");
  //Clear out the text
  inside.text("");
  //Insert new computed age statistics into the table
  inside.append("li").text("Mean : " + String(mean));
  inside.append("li").text("Mode : " + String(mode));
  inside.append("li").text("Median : " + String(median));
  inside.append("li").text("Variance : " + String(variance));
  inside.append("li").text("standard deviation : " + String(stddev));
  inside.append("li").text("N : " + String(allAges.length));
*/
});

// YOUR CODE HERE!



//For Later USE

//Loop through data
function DisplayTableRowsLooped(tableData){
    var row = tbody.append("tr");
    var theKeys = Object.keys(tableData);
    for (var i = 0; i <theKeys.length; i = i + 1){
        row.append("td").text(someData[theKeys[i]]);
    }
}

data.forEach(DisplayTableRowsLooped);

