var http = require('http');

// dados teste para testar o merge
var gitlab_mergerequest_body = {
    'object_attributes': {
        'target_project_id': 42,
        'target_branch': 'master',
        'merge_status': 'can_be_merged',
        'source_branch': 'postgres-ha-concluido',
        'created_at': '2014-08-05T14: 32: 32.575Z',
        'title': 'PostgresHaConcluido',
        'updated_at': '2014-08-05T14: 32: 33.522Z',
        'assignee_id': 'None',
        'iid': 20,
        'state': 'opened',
        'author_id': 13,
        'milestone_id': 'None',
        'id': 33,
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
