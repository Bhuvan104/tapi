function fetchMyData() {
    fetch('/data/')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Do something with the data, such as update the DOM
        })
        .catch(error => console.error(error));
}
