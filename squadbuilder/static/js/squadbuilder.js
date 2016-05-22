var cost = 0;

//The following variables are defined in builder.html based on query data from views.py
//var upgrades = {{ upgrades|safe }}; A dict of {pilot:upgradeArray}
//var pilotCost = {{pilotCost|safe}}; A dict of {pilot:cost}
//var upgradeCardList = {{cards|safe}}; A dict of Upgrade card/cost sorted by type


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
				"<ul class='dropdown-menu' aria-labelledby='test'>");
		
			upgradeCardArray=Object.keys(upgradeCardList[upgrades[this.id][i]]);
			for (j=0; j<upgradeCardArray.length; j++){
				htmlString+= ("<li><a class='upgrade' id=" + upgrades[this.id][i] + ">" + upgradeCardArray[j] + "</a></li>");
				
			}
			htmlString+=("<li><a class='upgrade' id=" + upgrades[this.id][i] + ">None</a></li></ul>"+"</span>");
		
		}
		
		$("#squad").append("<div class=" + this.id + ">" + '<img src="/static/img/Pilots/' + this.id + '.jpg" height=259px width=200px>' + htmlString + "</div>");
		cost+=pilotCost[this.id];
		updateCostDisplay(cost);
		

	  } else {
		for (i=0; i<upgrades[this.id].length; i++){
			console.log(upgrades[this.id][i]+this.id);
			var upgradeCost = $("."+upgrades[this.id][i]+this.id).data("cost");
			if (upgradeCost != null){
				cost-=upgradeCost;
			}
			
		}
		$("div." +this.id).last().remove();
		cost-=pilotCost[this.id];
		updateCostDisplay(cost);
	  }
	});

	$(document.body).on('click','.upgrade',function(){
		console.log("Upgrade was clicked");
		
		var selectedUpgrade=$(this).text().replace(/\s/g,"");
		var pilot=$(this).closest('div').attr('class');
		var upgradeType = $(this).attr('id');
		var upgradeCost=0;
		
		if(selectedUpgrade=="None"){
			console.log("made it into none");
			upgradeCost=$("."+upgradeType+pilot).data("cost");
			if(upgradeCost == null){
				upgradeCost=0;
			}
			$("."+upgradeType+pilot).remove();
			updateCostDisplay(cost-=upgradeCost);
			
		}
		else if($("."+upgradeType+pilot).length==0){
			upgradeCost=upgradeCardList[upgradeType][$(this).text()]['cost'];
			$("."+pilot).append('<span class=' + upgradeType + pilot + '> <img id=' + selectedUpgrade +' src="/static/img/Upgrades/' +selectedUpgrade+'.jpg" height=209px width=150px></span>');
			$("."+upgradeType+pilot).data("cost", upgradeCost);
			updateCostDisplay(cost+=upgradeCost);
		}
		else{
			upgradeCost=$("."+upgradeType+pilot).data("cost");
			updateCostDisplay(cost-=upgradeCost);
			$("."+upgradeType+pilot).remove();
			
			upgradeCost=upgradeCardList[upgradeType][$(this).text()]['cost'];
			$("."+pilot).append('<span class=' + upgradeType + pilot + '> <img id=' + selectedUpgrade +' src="/static/img/Upgrades/' +selectedUpgrade+'.jpg" height=209px width=150px></span>');
			$("."+upgradeType+pilot).data("cost", upgradeCost);
			updateCostDisplay(cost+=upgradeCost);
		}
		
		
		
	});
});

function updateCostDisplay(newvalue){
	$("#cost").text(newvalue+"/100");
}

$('select').on('change',function(){
	console.log("something changed");
	var numOfExpansions = $(".expansion-qty").length;
	var expansionQtyList = [];
	for(i=1;i<=numOfExpansions;i++){
		expansionQtyList+=$("#"+i+"select option:selected").text();
	}
	$('input[name="expansionCode"]').val(expansionQtyList);
});