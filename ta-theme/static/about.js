document.onload = function() {
    var data = {
        labels: ["Python", "Java", "PHP", "Javascript", "HTML", 'CSS', 'UX', 'Design'],
        datasets: [
            {
               label: "My First dataset",
               fillColor: "rgba(143,199,152,0.2)",
               strokeColor: "rgba(220,220,220,1)",
               pointColor: "rgba(68,153,220,1)",
               pointStrokeColor: "#fff",
               pointHighlightFill: "#fff",
               pointHighlightStroke: "rgba(220,220,220,1)",
               data: [65, 59, 90, 81, 56, 55, 40]
           }
        ]
    };
    var ctx = document.getElementById('languages').getContext('2d');
    var langsChart = new Chart(ctx).Radar(data);
}
