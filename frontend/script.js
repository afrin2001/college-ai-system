async function send(){
let msg = document.getElementById("msg").value;

let res = await fetch("http://127.0.0.1:5000/chat",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({message:msg})
});

let data = await res.json();

document.getElementById("messages").innerHTML +=
"<p><b>You:</b> "+msg+"</p><p><b>Bot:</b> "+data.response+"</p>";

document.getElementById("msg").value="";
}
