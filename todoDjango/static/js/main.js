console.log('hello via js')


$(document).ready(function(){
    $("#createButton").click(function(){
        var serializedData = $("#createTaskForm").serialize();
        
        $.ajax({
            url: $("createTaskForm").data('url'),
            data: serializedData,
            type: 'post',
            success: function(response){
                $("#taskList").append('<div class="card mb-3"><div class="card-body  position-relative">'+ response.task.title + '<button type="button" class="btn-close" ></button></div></div>')
            }
        });
    });

});