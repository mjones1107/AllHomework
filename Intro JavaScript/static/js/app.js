//Javascript Homework
// from data.js
var tableData = data;
console.log(tableData);

var tbody = d3.select("tbody");

data.forEach((tableData) => {
  var row = tbody.append("tr");
  Object.entries(tableData).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value);
  });
});


//Set up filter

// Select the submit button
var submit = d3.select("#submit");

submit.on("click", function() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#datetime");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);
  console.log(tableData);

  var filteredData = tableData.filter(tableData => tableData.datetime === inputValue);
  console.log(filteredData);


  var pickEvent = filteredData.map(tableData => tableData.datetime);
// Then, select the unordered list element by class name
  var list = d3.select(".table table-striped");

  // remove any children from the list to
  list.html("");

}); 















