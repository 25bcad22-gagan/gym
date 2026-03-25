async function addMember() {
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const plan = document.getElementById("plan").value;

    await fetch('/add_member', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, age, plan })
    });

    loadMembers();
}

async function loadMembers() {
    const response = await fetch('/get_members');
    const data = await response.json();

    const table = document.querySelector("#membersTable tbody");
    table.innerHTML = "";

    data.forEach(member => {
        const row = `
            <tr>
                <td>${member.id}</td>
                <td>${member.name}</td>
                <td>${member.age}</td>
                <td>${member.plan}</td>
            </tr>
        `;
        table.innerHTML += row;
    });
}

// Load members on page load
window.onload = loadMembers;