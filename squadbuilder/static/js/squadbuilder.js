var cost = 0;

//The following variables are defined in builder.html based on query data from views.py
//var upgrades = {{ upgrades|safe }}; A dict of {pilot:upgradeArray}
//var pilotCost = {{pilotCost|safe}}; A dict of {pilot:cost}


$(document).ready(function() {
// Put all your setup procedures here, this is sort of like your 'constructor' 
//  for initializing variables and finalizing the page after the client has 
//	finished loading.

$("#cost").text(cost +"/100");
console.log("ready!!");
$("#mytabs").click(function (e){
	console.log("made it into mytabs");
	$("input:checkbox").prop('checked', false);
	$("#squad").empty();
	cost = 0;
	updateCostDisplay(cost);
});
$(".pilotCheckbox").change(function() {
  // Attach an event to all objects with class pilotCheckbox change events
  if(this.checked) {
	var htmlString = "";
	
	for (i=0; i<upgrades[this.id].length; i++){
	htmlString += (
	"<span class='dropdown'>"+
		"<button type='button' class='btn btn-default dropdown-toggle' id='test' data-toggle='dropdown' aria-haspopup='true' aria-expanded='true'>"+ upgrades[this.id][i] + "</button>"+
		"<ul class='dropdown-menu' aria-labelledby='test'><li>Test1</li><li>Test2</li></ul>"+
	"</span>");
	}
	
	$("#squad").append("<div class=" + this.id + ">" + '<img src="/static/img/Pilots/' + this.id + '.jpg" height=209px width=150px>' + htmlString + "</div>");
	cost+=pilotCost[this.id];
	updateCostDisplay(cost);
	

  } else {
	$("div." +this.id).last().remove();
	cost-=pilotCost[this.id];
	updateCostDisplay(cost);
  }
});
});

function updateCostDisplay(newvalue){
	$("#cost").text(newvalue+"/100");
}
