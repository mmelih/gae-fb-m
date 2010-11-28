/*jslint browser: true */
function g(id) {
  return document.getElementById(id);
}

function makeRequest(target, method, request, args, callback) {
  var async, params, body, req, response, i;
  async = (callback !== null);

  // Build an Array of parameters, w/ function_name being the first parameter
  params = new Array(request);
  for (i = 0; i < args.length; i += 1) {
    params.push(args[i]);
  }
  body = JSON.stringify(params);

  // Create an XMLHttpRequest 'POST' request w/ an optional callback handler
  req = new XMLHttpRequest();
  req.open(method, target, async);

  if (async) {
    req.onreadystatechange = function () {
      if (req.readyState === 4 && req.status === 200) {
	response = null;
	try {
	 response = JSON.parse(req.responseText);
	} catch (e) {
	  response = req.responseText;
	}
	callback(response);
      }
    };
  }

  // Make the actual request
  req.send(body);
}

function postAjaxForm() {
  var target, method, request, callback, inputs, args, len, i;
  target = this.action;
  method = this.method;
  if (this.dataset) { // chrome
    request = this.dataset.request;
    callback = window[this.dataset.callback];
  }
  else { // firefox
    request = this.getAttribute("data-request");
    callback = window[this.getAttribute("data-callback")];
  }
  inputs = this.elements;
  args = [];
  len = inputs.length;
  for (i = 0; i < len; i += 1) {
    if (inputs[i].type !== 'submit') {
      args.push(inputs[i].value);
    }
  }
  makeRequest(target, "POST", request, args, callback);
  return false;
}

function showEntries(data) {
	var a = document.getElementById("ta");
	alert(data);
	
	var h = document.getElementById("et");
	et.innerHTML = data[0];
	var f = document.forms.ef.elements.t;
	f.value = data[0];
}
function appendEntry(entry) {
  var title = entry[0],
    content = entry[1];
  
  alert(title + content);
}

function showTitle(title) {
  window.location.hash = "#show?q=" + title;
  return;
}

window.onload = function () {
  var forms, len, i;
  forms = document.forms;
  len = forms.length;
  for (i = 0; i < len; i += 1) {
    forms[i].onsubmit = postAjaxForm;
  }
};