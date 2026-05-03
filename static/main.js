const popularItems = [
    { id: 1, title: "Type 2 Diabetes" },
    { id: 2, title: "Hypertension" },
    { id: 8, title: "COVID-19" }
];

$(document).ready(function() {

    if ($("#popular").length) {
        popularItems.forEach(item => {
            $("#popular").append(`
                <div>
                    <h4>${item.title}</h4>
                    <a href="/view/${item.id}">View Details</a>
                    <hr>
                </div>
            `);
        });
    }

    $("form").submit(function(event) {
        const input = $("#searchInput");
        if (input.val().trim() === "") {
            event.preventDefault();
            input.val("");
            input.focus();
        }
    });

});
