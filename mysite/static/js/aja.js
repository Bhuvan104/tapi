fetch('your_view')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));