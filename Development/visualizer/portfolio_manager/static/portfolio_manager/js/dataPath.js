var parseTime = d3.timeParse("%d-%b-%y");

var height = 500,
    width = 1000,
    marginY = 100,
    marginX = 100;

var svg = d3.select("body")
            .append("svg")
            .attr("height", height+marginX)
            .attr("width", width+marginY)
            .append("g")
            .attr("transform", "translate("+50+","+50+")");

//var pathData = [{"date": "01-05-16", "close": 50.10},
//                {"date": "01-06-16", "close": 100.03},
//                {"date": "01-07-16", "close": 200.04}];

d3.csv("data.csv", function(pathData){

var x = d3.scaleTime().range([0,width]),
    y = d3.scaleLinear().range([height,0]);

pathData.forEach(function(d) {
   d.date = parseTime(d.date);
   d.close = +d.close;
});

x.domain(d3.extent(pathData, function(d){return d.date}))
y.domain([0, d3.max(pathData, function(d){return d.close})])

var lineFunction = d3.line()
                     .x(function(d){return x(d.date);})
                     .y(function(d){return y(d.close);});

svg.append("path")
   .attr("class", "line")
   .attr("d", lineFunction(pathData));

svg.append("g")
   .attr("transform", "translate(0,"+height+")")
   .call(d3.axisBottom(x));
svg.append("g")
   .call(d3.axisLeft(y));

});
