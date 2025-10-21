document.getElementById("runButton").addEventListener("click", async () => {
    const language = document.getElementById("languageDropdown").value;
    const comments = document.getElementById("commentInput").value;
  
    const response = await fetch("/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ language, comments })
    });
  
    const result = await response.json();
    document.getElementById("codeOutput").textContent = result.code || "Error generating code.";
  });
  
  document.getElementById("clearButton").addEventListener("click", () => {
    document.getElementById("commentInput").value = "";
    document.getElementById("codeOutput").textContent = "// Your generated code will appear here...";
    document.getElementById("resultOutput").textContent = "// Your output will appear here...";
  });
  
  document.getElementById("downloadButton").addEventListener("click", () => {
    const code = document.getElementById("codeOutput").textContent;
    const language = document.getElementById("languageDropdown").value;
    const blob = new Blob([code], { type: "text/plain" });
    const link = document.createElement("a");
    link.download = `generated_code.${language}`;
    link.href = URL.createObjectURL(blob);
    link.click();
  });
  
  document.getElementById("guideButton").addEventListener("click", () => {
    window.open("https://docs.google.com/document/d/guide-link", "_blank");
  });
  