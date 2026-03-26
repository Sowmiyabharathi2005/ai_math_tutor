document.getElementById("form").onsubmit = async (e) => {

    e.preventDefault();

    let formData = new FormData(e.target);

    let res = await fetch("/solve", {
        method: "POST",
        body: formData
    });

    let data = await res.json();

    if (data.error) {
        document.getElementById("result").innerHTML = data.error;
        return;
    }

    let d = data.data;

    document.getElementById("result").innerHTML = `
        <h3>Equation: ${d.equation}</h3>
        <h3>LaTeX: ${d.latex}</h3>
        <h3>Steps:</h3>
        ${d.steps.map(s => `<p>${s}</p>`).join("")}
        <h3>Solution: ${d.solution}</h3>
        <h3>Mistakes:</h3>
        ${d.mistakes.map(m => `<p>${m}</p>`).join("")}
    `;
};