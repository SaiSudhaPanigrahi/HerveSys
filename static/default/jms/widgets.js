
function update(widget){
    $("#widgets").append('<div class="item"><div id="'+widget["element"].slice(1, -1)+'" class="card white shadows"><center><img src="/static/default/imgs/loader.gif"/></center></div></div>')
    log>widget["url"].replace("%2F","/");
    $.get(widget["url"].replace("%2F","/"), function(datas) {
        var html = $('<div/>').append(jQuery.parseHTML(datas)).find(widget["element"]).html();
        if (html != undefined){
            $("#"+widget["element"].slice(1, -1)).html(html);
        }
    });
}
$(function() {
    $.get("/list/widgets", {}, function(widgets) {
        for(var i = 0; i< widgets.length; i++) {
            widget = widgets[i].split(" ");
            widget = {
                    "element": widget[0],
                    "url": widget[1]
                }
            update(widget);
        }
    });
});