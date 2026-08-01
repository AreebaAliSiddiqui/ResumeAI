    const form = document.getElementById("generate-form");

    
    const generateBtn = document.getElementById("generate-btn");

    function handleSubmit(event) {
        generateBtn.textContent = 'Generating resume...'; 
        generateBtn.disabled = true; }
        

    form.addEventListener("submit", handleSubmit );
    