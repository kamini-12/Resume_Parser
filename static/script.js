document.getElementById("uploadForm").addEventListener("submit", function(event) {
    event.preventDefault();
    let formData = new FormData();
    formData.append("resume", document.getElementById("resume").files[0]);
    
    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    })
    .catch(error => console.error("Error:", error));
});
