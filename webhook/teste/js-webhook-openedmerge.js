var http = require('http');

// dados teste para testar o merge
var gitlab_mergerequest_body = {
  "object_kind": "merge_request",
  "object_attributes": {
    "id": 99,
    "target_branch": "master",
    "source_branch": "ms-viewport",
    "source_project_id": 14,
    "author_id": 51,
    "assignee_id": 6,
    "title": "MS-Viewport",
    "created_at": "2013-12-03T17:23:34Z",
    "updated_at": "2013-12-03T17:23:34Z",
    "st_commits": null,
    "st_diffs": null,
    "milestone_id": null,
    "state": "opened",
    "merge_status": "unchecked",
    "target_project_id": 14,
    "iid": 1,
    "description": ""
  }
};

var mergereqString = JSON.stringify(gitlab_mergerequest_body);

var headers = {
  'Content-Type': 'application/json',
  'Content-Length': mergereqString.length
};

var options = {
  host: '127.0.0.1',
  port: 5000,
  method: 'POST',
  headers: headers
};

// testa envio de dados "merge"
var req = http.request(options, function(res) {
  res.setEncoding('utf-8');

  var responseString = '';

  res.on('data', function(data) {
    responseString += data;
  });

  res.on('end', function() {
    var resultObject = JSON.parse(responseString);
    console.log(responseString);
  });
});

req.on('error', function(e) {
  // TODO: handle error.
  console.log('ocorreu erro: ' + e);
});

req.write(mergereqString);
req.end();

