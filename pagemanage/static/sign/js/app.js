$(function() {

        var $fullText = $('.admin-fullText');
        $('#admin-fullscreen').on('click', function() {
            $.AMUI.fullscreen.toggle();
        });

        $(document).on($.AMUI.fullscreen.raw.fullscreenchange, function() {
            $fullText.text($.AMUI.fullscreen.isFullscreen ? '退出全屏' : '开启全屏');
        });


        // var dataType = $('#tpl-echarts').attr('data-type');
        // for (key in pageData) {
        //     if (key == dataType) {
        //         //pageData[key]();
        //     }
        // }

        $('.tpl-switch').find('.tpl-switch-btn-view').on('click', function() {
            $(this).prev('.tpl-switch-btn').prop("checked", function() {
                    if ($(this).is(':checked')) {
                        return false
                    } else {
                        return true
                    }
                })
                // console.log('123123123')

        })
    })
    // ==========================
    // 侧边导航下拉列表
    // ==========================

$('.tpl-left-nav-link-list').on('click', function() {
        $(this).siblings('.tpl-left-nav-sub-menu').slideToggle(80)
            .end()
            .find('.tpl-left-nav-more-ico').toggleClass('tpl-left-nav-more-ico-rotate');
    })
    // ==========================
    // 头部导航隐藏菜单
    // ==========================

$('.tpl-header-nav-hover-ico').on('click', function() {
    $('.tpl-left-nav').toggle();
    $('.tpl-content-wrapper').toggleClass('tpl-content-wrapper-hover');
})


// 页面数据
var pageData = {
    // ===============================================
    // 首页
    // ===============================================
    'index': function indexData() {

        var echartsC = echarts.init(document.getElementById('tpl-echarts'));

        optionC = {
            tooltip: {
                trigger: 'axis'
            },
            toolbox: {
                top: '0',
                feature: {
                    dataView: { show: true, readOnly: false },
                    magicType: { show: true, type: ['line', 'bar'] },
                    restore: { show: true },
                    saveAsImage: { show: true }
                }
            },
            legend: {
                data: ['任务', '接口', '用例']
            },
            grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
            },
            xAxis: [{
                type: 'category',
                data: ['2018/03/07', '2018/03/08', '2018/03/09', '2018/03/10', '2018/03/11', '2018/03/12', '2018/03/13']
            }],
            yAxis: [{
                    type: 'value',
                    name: '数量',
                    min: 0,
                    axisLabel: {
                        formatter: '{value}'
                    }
                }],
            series: [
                {
                    name: '任务',
                    type: 'line',
                    data: [0, 1, 1, 1, 1, 1, 1]
                },
                {
                    name: '接口',
                    type: 'line',
                    data: [0, 10, 12, 12, 34, 40, 41]
                },
                {
                    name: '用例',
                    type: 'line',
                    data: [0, 1, 3, 9, 9, 10, 14]
                }
            ]
        };
        echartsC.setOption(optionC);
    }
}