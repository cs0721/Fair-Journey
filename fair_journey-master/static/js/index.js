let table = $('#datatables').DataTable({
    "processing": true,
    "serverSide": true,
    "ajax": {
        "url": "/api/road/",
        "type": "GET"
    },
    "columns": [
        {"data": "rwe_type"},
        {"data": "rwe_closure_type"},
        {"data": "rwe_status"},
        {"data": "rwe_start_dt"},
        {"data": "rwe_end_dt"},
        {"data": "rwe_publish_text"},
        {"data": "subject_pref_rdname"},
        {"data": "traffic_delay"},
        {"data": "speed_limit"},
        {"data": "lanes_affected"},

    ]
});




