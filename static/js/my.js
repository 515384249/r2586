//自动调整div高度
// $(document).ready(function(){
//     $('#sidebar').css("height",$('.diyilie').height())
//
// }


//删除
$(document).ready(function () {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // 删除
    $('#btn_delete').click(function () {


        var id_array = new Array();
        $('input[name="subbox"]:checked').each(function () {
            id_array.push($(this).attr('id'));//向数组中添加元素
        });
        var idstr = id_array.join(',');//将数组元素连接起来以构建一个字符串
        // alert(idstr);


        // var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        $.ajax({

            type: "POST",
            data: {

                "type": "del",
                "data": idstr,
            },
            url: '/comments_upload/', //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
            cache: false,

            dataType: "html",
            success: function (result) {
                alert(result);                                         //成功时弹出view传回来的结果
                window.location.reload();
            },
            error: function () {
                alert("false");
            }
        });
        return false;
    });

});


//新增
$(document).ready(function () {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    $('#btn_add').click(function () {


        var id_array = new Array();
        $('input[name="subbox"]:checked').each(function () {
            id_array.push($(this).attr('id'));//向数组中添加元素
        });
        var idstr = id_array.join(',');//将数组元素连接起来以构建一个字符串
        // alert(idstr);


        // var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        $.ajax({

            type: "POST",
            data: {

                "type": "new",
                "data": idstr,
            },
            url: '/comments_upload/', //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
            cache: false,

            dataType: "html",
            success: function (result) {
                alert("tiaozhuan");
                window.location.href = result.valueOf();
            },
            error: function () {
                alert("false");
            }
        });
        return false;
    });

});


//快捷查询
$(document).ready(function () {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    // language=JQuery-CSS
    $('.list-group-item').click(function () {
        var idstr = $(this).html()
        var s = ""


        // var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        $.ajax({

            type: "POST",
            data: {

                "type": "kjjs",
                "data": idstr,
            },
            url: '/kjfs_search/', //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
            cache: false,

            dataType: "json",
            success: function (result) {
                // result = JSON.parse(result)

                for (var i = 0; i < result.length; i++) {
//                             s =s+ "<tr><td>"+result[i].fields.yuan+"</td>"+"</td>" +"<td>"+result[i].fields.xi+"</td>"+"<td>"+result[i].fields.xi+"</td>"+
//                                "<td>"+result[i].fields.zhuanye+"</td>" +"<td>"+result[i].fields.xingming+"</td>"+"<td>"+result[i].fields.zhiwu+"</td>"+
// "<td>"+result[i].fields.dianhua+"</td>"  +"<td>"+result[i].fields.dizhi+"</td>"+
//                             "</tr>"
//                         }
                    s = s + "<tr><td>" + result[i].yuan + "</td>"  + "<td>" + result[i].xi + "</td>" +
                        "<td>" + result[i].zhuanye + "</td>" + "<td>" + result[i].xingming + "</td>" + "<td>" + result[i].zhiwu + "</td>" +
                        "<td>" + result[i].dianhua + "</td>" + "<td>" + result[i].dizhi + "</td>" +
                        "</tr>"
                }
                $("#mytable").html(s)


            },
            error: function () {
                alert("false");
            }
        });
        return false;
    });

});

//编辑
$(document).ready(function () {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            function csrfSafeMethod(method) {
                // these HTTP methods do not require CSRF protection
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                var csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    $('#btn_edit').click(function () {


        var id_array = new Array();
        $('input[name="subbox"]:checked').each(function () {
            id_array.push($(this).attr('id'));//向数组中添加元素
        });
        var idstr = id_array.join(',');//将数组元素连接起来以构建一个字符串
        // alert(idstr);


        // var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        $.ajax({

            type: "POST",
            data: {

                "type": "new",
                "data": idstr,
            },
            url: '/comments_upload/', //后台处理函数的url 这里用的是static url 需要与urls.py中的name一致
            cache: false,

            dataType: "html",
            success: function (result) {
                alert("tiaozhuan");
                window.location.href = result.valueOf();
            },
            error: function () {
                alert("false");
            }
        });
        return false;
    });

});



