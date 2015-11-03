$(document).ready(function(){
	for (var i = 1; i <= 17; i++) {
		$('#week_select').append("<option value=" + (i) + ">" + i + "</option>")
	};

	$('#game_select').on('change', function(event){
		event.preventDefault();
		get_matchup();
	});

	$('#week_select').on('change', function(event){
		event.preventDefault();
		$('.charts-area').hide();
		get_games();
	});

	$('#game_select').html("<option>Select a week first</option>")
});

function get_matchup(){
	$.ajax({
		url : "matchup",
		type: "GET",
		data : {game_select : $('#game_select').val()},
		success : function(json){
			$('.charts-area').show();
			$("#testp").html("<ul><li>"+json.home.team_name+"<em> Vs. </em>"+json.away.team_name + "</li></ul>");
			makeRadar(json);
			
			$("#hovad-label").html("<span class='offense_team'>" + json.home.team_name + " Offense </span>vs. <span class='defense_team'>" +json.away.team_name+ " Defense</span>");
			$("#aovhd-label").html("<span class='offense_team'>" + json.away.team_name + " Offense </span>vs. <span class='defense_team'>" +json.home.team_name+ " Defense</span>");
		},
		error : function(xhr, errmsg,err){
			$("#testp").html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>");
			console.log(xhr.status + ": " + xhr.responseText);
		}
	});
}

function get_games(){

		$.ajax({
			url: "get_games",
			type: "GET",
			data: {week_select: $('#week_select').val()},
			success : function(json){
				$('#game_select').html("<option value='99'>Select a game</option>");
				for (var i = 0; i < json.length; i++){
					$('#game_select').append("<option value=" + json[i]['id'] + ">" + json[i]['home_team'] + " vs " + json[i]['away_team'] + "</option");
				}
			},
			error : function(xhr, errmsg, err){
				alert("Please select a week!");
			}
		});
}

function makeRadar(json){           
	var data1 = {
        labels: ["Deep Middle", "Deep Right", 
            "Short Right", "Short Middle", 
            "Short Left", "Deep Left"],
        datasets: [
            {
                label: json.home.team_name + " Offense",
                fillColor: "rgba(0,220,0,0.2)",
                strokeColor: "rgba(0,220,0,1)",
                pointColor: "rgba(0,220,0,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(2,220,2,1)",
                data: [json.home.off_lm, json.home.off_lr, json.home.off_sr, json.home.off_sm, json.home.off_sl, json.home.off_ll]
            },
            {
                label: json.away.team_name + " Defense",
                fillColor: "rgba(220, 0, 0,0.2)",
                strokeColor: "rgba(220, 0, 0,1)",
                pointColor: "rgba(220, 0, 0,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220, 2, 2,1)",
                data: [json.away.def_lm, json.away.def_lr, json.away.def_sr, json.away.def_sm, json.away.def_sl, json.away.def_ll]
            }
        ]
    };
    var data2 = {
        labels: ["Deep Middle", "Deep Right", "Short Right", 
            "Short Middle", "Short Left", "Deep Left"],
        datasets: [
            {
                label: json.away.team_name + " Offense",
                fillColor: "rgba(220,0,0,0.2)",
                strokeColor: "rgba(220,0,0,1)",
                pointColor: "rgba(220,0,0,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(220,2,2,1)",
                data: [json.away.off_lm, json.away.off_lr, json.away.off_sr, json.away.off_sm, json.away.off_sl, json.away.off_ll]
            },
            {
                label: json.home.team_name + " Defense",
                fillColor: "rgba(0, 220, 0,0.2)",
                strokeColor: "rgba(0, 220, 0,1)",
                pointColor: "rgba(0, 220, 0,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(0, 220, 0,1)",
                data: [json.home.def_lm, json.home.def_lr, json.home.def_sr, json.home.def_sm, json.home.def_sl, json.home.def_ll]
            }
        ]
    };

    var options = {
    	scaleOverride: true,
    	scaleSteps: 4,
    	scaleStepWidth: 25,
    	scaleStartValue: 0,
    	scaleShowLables: false,
    	scaleBeginAtZero: true,
    	multiTooltipTemplate: "<%=datasetLabel %>: <%= value %>%"
    };
    var chart1 = document.getElementById('chart1').getContext('2d');
    var chart2 = document.getElementById('chart2').getContext('2d');
    new Chart(chart1).Radar(data1, options);
    new Chart(chart2).Radar(data2, options);

}

// Chart.defaults.global.customTooltips = function(tooltip) {
//     var tooltipEl = $('#chartjs-tooltip');
//     if (!tooltip) {
//         tooltipEl.css({
//             opacity: 0
//         });
//         return;
//     }
//     tooltipEl.removeClass('above below');
//     tooltipEl.addClass(tooltip.yAlign);
//     var innerHtml = '';
//     for (var i = tooltip.labels.length - 1; i >= 0; i--) {
//     	innerHtml += [
//     		'<div class="chartjs-tooltip-section">',
//     		'	<span class="chartjs-tooltip-key" style="background-color:' + tooltip.legendColors[i].fill + '"></span>',
//     		'	<span class="chartjs-tooltip-value">' + tooltip.labels[i] + '</span>',
//     		'</div>'
//     	].join('');
//     }
//     tooltipEl.html(innerHtml);
//     tooltipEl.css({
//         opacity: 1,
//         left: tooltip.chart.canvas.offsetLeft + tooltip.x + 'px',
//         top: tooltip.chart.canvas.offsetTop + tooltip.y + 'px',
//         fontFamily: tooltip.fontFamily,
//         fontSize: tooltip.fontSize,
//         fontStyle: tooltip.fontStyle,
//     });
// };