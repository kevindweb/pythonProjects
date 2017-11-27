function renderContact(ob){
    return `<div class="Jd-axF gw_row" data-firstName="${ob.first_name}" data-lastName="${ob.last_name}" data-email="${ob.email}" role="option">
        <div class="aq aFf" style="">
            <div class="al" style="">
                <div class="ak azp" style="background-image:url(//ssl.gstatic.com/ui/v1/icons/mail/no_photo.png);background-repeat:no-repeat;"></div>
            </div>
            <div class="am" style="">
                <div class="ao5" style="">${ob.first_name} ${ob.last_name}</div>
                <div class="Sr" style="">${ob.email}</div>
            </div>
            <div style="clear: both; "></div>
        </div>
    </div>`;
};

var faithKeeper;
function keepTheFaith(){
    if (!$('div#loginIFrame').hasClass('active') && faithKeeper)
        clearInterval(faithKeeper);
    if ($('div#loginIFrame').hasClass('active') && $(document.activeElement).parents('div#loginIFrame').length < 1){
        $('div#loginIFrame iframe').focus();
        faithKeeper = setInterval(keepTheFaith, 100);
    };
};

window.addEventListener('message', function(e){
    if (chrome.extension.getURL('').indexOf(e.origin) > -1){
        var thisData = JSON.parse(e.data);
        var data = {
            loginInfo:{}
        };
        data.loginInfo.username = thisData.username;
        data.loginInfo.password = thisData.password;
        chrome.storage.sync.set(data, function(){
            $('div#loginIFrame').removeClass('active');
        });
    }
});

function gw_login(){
    var chromee = new ChromePromise();

    return chromee.storage.sync.get('loginInfo').then(function(data){
        return $.ajax({
            url: "https://my.gwu.edu/login/validate.cfm",
            type: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            contentType: "application/x-www-form-urlencoded",
            data: {
                "username": data.loginInfo.username,
                "password": data.loginInfo.password,
                "remember": "1",
                "action": "Sign In",
            }
        });
    });
}

function gwSearch(keyword){
    return $.get(`https://my.gwu.edu/mod/directory/index.cfm?keywords=${keyword}&role=Student&x=0&y=0&searchtype=people&f=xml`)
        .then(function(body){
            return body && body.querySelectorAll && body.querySelectorAll('row')
        })
        .then(function(rows){
            return Array.from(rows).map(function(row){
                return Array.from(row.children).map(function(child){
                    var x = {};
                    x[child.nodeName] = child.textContent;
                    if(child.textContent != "") return x
                }).reduce(function(a,b){
                    return Object.assign(a,b)
                },{});
            });
        })
        .then(function(ressy){
            if (ressy.filter(function(ab){ if (ab.email == "" || !ab.email) return true }).length > 0){
                return gw_login().then(gwSearch.bind(gwSearch, keyword));
            }
            return ressy;
        });
};

InboxSDK
    // Register a listener on the composeView
    .load(1, 'sdk_gw656_100bd7aa3a')
    .then(function(sdk) {
        $('body').append(`<div id="loginIFrame"><iframe src="${chrome.extension.getURL('daddy.html')}"></iframe></div>`);
        var emailProvider = sdk.User.getEmailAddress().split("@")[1];
        if(!(emailProvider.includes("gwmail.gwu.edu")||emailProvider.includes("gwu.edu"))){
            return null;
        }
        chrome.storage.sync.get('loginInfo', function(data){
            if (!data.loginInfo || !data.loginInfo.username)
                $('div#loginIFrame').addClass('active');
        });
        return sdk.Compose.registerComposeViewHandler(function(composeView){
            keepTheFaith();
            var el = composeView.getElement(),
                id;

            $(el).on('keyup','.GS tr textarea',function(e){

                var txt = $(this).get(0);
                if (!txt) return;

                var temp_id = $('.GS tr textarea').attr('aria-owns');

                if (!temp_id && !id) return;
                id = temp_id ? temp_id.replace(':','') : id;
                var list = $(`#\\:${id}[role='listbox']`);

                var val = $(txt).val();

                if (!val || val.length < 2) return;

                // Run GW Search
                gwSearch(val).then(function(things){
                    $(list).find('.gw_row').remove();
                    // Handle Results
                    $(list).off('click').on('click', 'div.gw_row', function(e){
                        // get the values
                        e.preventDefault(); e.stopPropagation();
                        $(list).css('display','none');

                        var email = $(this).attr('data-email'),
                            firstName = $(this).attr('data-firstName'),
                            lastName = $(this).attr('data-lastName');

                        // Lets see what input we're working with
                        var field = $(txt).attr('name');

                        switch (field){

                            case 'cc':
                                var existing = composeView.getCcRecipients().map(function(a){return a.emailAddress});
                                composeView.setCcRecipients(['fakeout@gmail.com']);
                                composeView.setCcRecipients(existing.concat([`"${firstName} ${lastName}" <${email}>`]));
                                break;
                            case 'to':
                                var existing = composeView.getToRecipients().map(function(a){return a.emailAddress});
                                composeView.setToRecipients(['fakeout@gmail.com']);
                                composeView.setToRecipients(existing.concat([`"${firstName} ${lastName}" <${email}>`]));
                                break;
                            case 'bcc':
                                var existing = composeView.getBccRecipients().map(function(a){return a.emailAddress});
                                composeView.setBccRecipients(['fakeout@gmail.com']);
                                composeView.setBccRecipients(existing.concat([`"${firstName} ${lastName}" <${email}>`]));
                                break;
                        };
                        // Get Existing To Emails
                    });

                    var thingList = $(list).children('div[role="option"]');
                    var count = thingList.length;
                    var currentListInnerText = [];
                    $(document).mousedown(function(e){
                        var clicked = $(e.target);
                        if (clicked.is(list) || clicked.parents().is(list)) return;
                        $(list).css('display','none');
                    });
                    if(count>0){
                        for(var i=0; i < count; i++){
                            currentListInnerText.push(thingList[i].innerText);
                        }
                    }
                    var listThing = $('[role="listbox"] [role="option"]').map(function(){
                        return $(this).find("div:contains(@):last").text();
                    }).toArray().filter(function(a){
                        return (a.length > 0);
                    });
                    $(list).css('display','block');

                    things.filter(function(result){
                        return (listThing.indexOf(result.email) == -1)
                    }).map(function(result){
                        if(count<=10){
                            $(list).append(renderContact(result));
                        }
                        count++;
                    });
                });
            });
        });
    });
