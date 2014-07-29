var http = require('http');

// dados teste para testar o merge
var gitlab_mergerequest_body = {
    'object_attributes': {
        'target_project_id': 98,
        'target_branch': 'master',
        'source_branch': 'bla',
        'created_at': '2014-07-29T16: 42: 10.557Z',
        'title': 'Bla',
        'updated_at': '2014-07-29T16: 43: 16.063Z',
        'assignee_id': "None",
        'iid': 5,
        'merge_status': 'cannot_be_merged',
        'state': 'closed',
        'author_id': 31,
        'milestone_id': "None",
        'id': 33,
        'source_project_id': 98,
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
