var YEARS = 4.8,  
    canvas = document.getElementById('languages'),
    ctx = canvas.getContext('2d'),
    skills = {
        "Backend Development": 5,
        "Frontend Development": 3.8, 
        'Mobile (Android)': 1,
        "UX/UI Design": 4,
        "Graphic Design": 2, 
        "Sys Admin": 4
    }, 
    labels = [], 
    values = [],
    data,
    skillsChart;

for(var k in skills) {
    if ( skills.hasOwnProperty(k) ) {
        labels.push(k);
        values.push(skills[k]);
    }
}

data = {
    labels: labels,
    datasets: [
        {
            label: "Months of Experience",
            fillColor: "rgba(68,153,142,0.2)",
            strokeColor: "rgba(143,199,152,1)",
            pointColor: "rgba(143,199,152,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: values,
        }
    ]
};

skillsChart = new Chart(ctx).Radar(data);
canvas.onclick = function(e) {
    var activePoints = skillsChart.getPointsAtEvent(e);
};
