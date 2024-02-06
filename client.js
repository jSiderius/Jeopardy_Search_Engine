// Listens for the enter key to be pressed, then sends a fetch request to the server with the search message taken from the searchInput field, and displays the results on the page
document.getElementById('searchInput').addEventListener('keypress', async (event) => {
  try {
    if (event.key === 'Enter') {
      const message = document.getElementById('searchInput').value;
      const url = "http://localhost:8080/search?message=" + message;
      const response = await fetch(url, { mode: 'cors' });

      if (!response.ok) throw new Error(response.statusText);

      const result = await response.json();
      displayResults(result);
    }
  } catch (error) {
    console.log(error);
  }
});

// Listens for the search button to be pressed, then sends a fetch request to the server with the search message taken from the searchInput field, and displays the results on the page
document.getElementById('searchButton').addEventListener('click', async () => {
  try {
    const message = document.getElementById('searchInput').value;
    const url = "http://localhost:8080/search?message=" + message;
    const response = await fetch(url, {mode: 'cors'});
    if(!response.ok) throw new Error(response.statusText);
    const result = await response.json();
    displayResults(result);

  } catch (error) {
    console.log(error);
  }
});

// Function to display the results of the search
function displayResults(results) {
  console.log("displayResults()");
  console.log(results);
  
  var resultsContainer = document.getElementById('searchResults');
  resultsContainer.innerHTML = "";
  // Create table element
  var table = document.createElement('table');
  table.classList.add('excel-grid');
  // Create table header
  var headerRow = document.createElement('tr');
  var headerCell1 = document.createElement('th');
  var headerCell2 = document.createElement('th');
  var headerCell3 = document.createElement('th');
  var headerCell4 = document.createElement('th');
  var headerCell5 = document.createElement('th');
  var headerCell6 = document.createElement('th');
  var headerCell7 = document.createElement('th');
  headerCell1.textContent = 'Question';
  headerCell2.textContent = 'Answer';
  headerCell3.textContent = 'Category';
  headerCell4.textContent = 'Value';
  headerCell5.textContent = 'Round';
  headerCell6.textContent = 'Air Date';
  headerCell7.textContent = 'Show Number';

  headerRow.appendChild(headerCell1);
  headerRow.appendChild(headerCell2);
  headerRow.appendChild(headerCell3);
  headerRow.appendChild(headerCell4);
  headerRow.appendChild(headerCell5);
  headerRow.appendChild(headerCell6);
  headerRow.appendChild(headerCell7);
  table.appendChild(headerRow);

  // Iterate through results and create table rows
  for (var key in results) {
      var row = document.createElement('tr');

      // Create cells for each result
      var cell1 = document.createElement('td');
      var cell2 = document.createElement('td');
      var cell3 = document.createElement('td');
      var cell4 = document.createElement('td');
      var cell5 = document.createElement('td');
      var cell6 = document.createElement('td');
      var cell7 = document.createElement('td');
      cell1.textContent = results[key]['Question'];
      cell2.textContent = results[key]['Answer'];
      cell3.textContent = results[key]['Category'];
      cell4.textContent = results[key]['Air_Date'];
      cell5.textContent = results[key]['Value'];
      cell6.textContent = results[key]['Round'];
      cell7.textContent = results[key]['Show_Number'];
      // Append cells to the row
      row.appendChild(cell1);
      row.appendChild(cell2);
      row.appendChild(cell3);
      row.appendChild(cell4);
      row.appendChild(cell5);
      row.appendChild(cell6);
      row.appendChild(cell7);
      // Append row to the table
      table.appendChild(row);
  }
  // Append the table to the results container
  resultsContainer.appendChild(table);
}

