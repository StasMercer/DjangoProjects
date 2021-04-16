function markClick(e, id) {
    if (e.target.classList.contains("mark-red")) {
        $.post("/mark_user/", {id: id, bg_color: "bg-danger"}).done(function (data) {
            if (data === 'ok') {
                location.reload();
            }
        });
    }

    if (e.target.classList.contains("mark-yellow")) {
        $.post("/mark_user/", {id: id, bg_color: "bg-warning"}).done(function (data) {
            if (data === 'ok') {
                location.reload();
            }
        });
    }

    if (e.target.classList.contains("mark-light")) {
        $.post("/mark_user/", {id: id, bg_color: "bg-light"}).done(function (data) {
            if (data === 'ok') {
                location.reload();
            }
        });
    }

}