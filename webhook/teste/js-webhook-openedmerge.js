var http = require('http');

// dados teste para testar o merge
var gitlab_mergerequest_body = {
    'object_attributes': {
        'target_project_id': 42,
        'target_branch': 'master',
        'merge_status': 'can_be_merged',
        'source_branch': 'teste',
        'created_at': '2014-08-07T15: 24: 56.404Z',
        'title': 'Teste',
        'updated_at': '2014-08-07T15: 26: 15.752Z',
        'assignee_id': None,
        'iid': 45,
        'state': 'opened',
        'author_id': 13,
        'milestone_id': None,
        'id': 58,
        'source_project_id': 42,
        'description': ''
    },
    'object_kind': 'merge_request'
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
