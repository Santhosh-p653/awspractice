async function loadMessage() {
    const res = await fetch("http://127.0.0.1:5000/api/message");
    const data = await res.json();
    document.getElementById("result").innerText = data.message;
}