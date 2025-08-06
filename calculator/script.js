function generateHashtags() {
  let input = document.getElementById("keywordInput").value;
  let output = document.getElementById("output");
  if (input) {
    output.innerHTML = "#" + input.split(" ").join(" #");
  }
  else {
    output.innerHTML = "<p style='color: red;'>Please enter the text to generate the hashtag</p>";
    return;
  }
}

function copyHashTags() {
  let text = document.getElementById("output").innerText;

  if (text.trim()) {
    navigator.clipboard.writeText(text);
    alert("Hashtags copied to clipboard!");
  }
  else {
    alert("No message was copied");
  }
}