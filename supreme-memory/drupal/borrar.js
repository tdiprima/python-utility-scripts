// jQuery
function getCsrfToken(callback) {
  jQuery
      .get('https://quip.bmi.stonybrook.edu/rest/session/token')
      .done(function (data) {
        var csrfToken = data;
        console.log('Token:', csrfToken);
        callback(csrfToken);
      });
}

function deleteNode(csrfToken) {
  jQuery.ajax({
    url: 'https://quip.bmi.stonybrook.edu/node/28134',
    method: 'DELETE',
    headers: {
      'X-CSRF-Token': csrfToken
    },
    success: function () {
      console.log('Node deleted.');
    }
  });
}

// getCsrfToken(function (csrfToken) {
//   deleteNode(csrfToken);
// });

function getData() {
  jQuery.getJSON('https://quip.bmi.stonybrook.edu/listofimages/23?_format=json', function (data) {
    $.each(data, function (key, entry) {
      let nid = entry.nid[0].value;
      document.write('https://quip.bmi.stonybrook.edu/maps/' + nid + '?_format=json<br>');
      const url = '/maps/' + nid + '?_format=json';
      jQuery.getJSON(url, function (data) {
            try {
              if (data[0]) {
                // TODO: NOTE, FIELDMAP TARGETID IS *NOT* THE MAP ID!
                // let map_id = data[0].field_map[0].target_id;
                let map_id = m['nid'][0]['value']
                let m_url = data[0].field_map[0].url;
                if (m_url.includes("2019-11")) {
                  document.write(m_url + '<br>');
                  document.write(map_id + '<br>');
                  // jQuery
                  //     .get('https://quip.bmi.stonybrook.edu/rest/session/token')
                  //     .done(function (data) {
                  //       var csrfToken = data;
                  //       console.log('Token:', csrfToken);
                  //       jQuery.ajax({
                  //         url: 'https://quip.bmi.stonybrook.edu/node/' + map_id,
                  //         method: 'DELETE',
                  //         headers: {
                  //           'X-CSRF-Token': csrfToken
                  //         },
                  //         success: function () {
                  //           console.log('Node ' + map_id + ' deleted.');
                  //         }
                  //       });
                  //     });
                }
              } else {
                document.write('What happened? ', url, '<br>')
              }
            } catch (e1) {
              console.error('e1', e1)
            }
          }
      );

    })
  });
}

getData();

/*
// cURL (command line)
curl --include \
  --request DELETE \
  --user USER:PASSWD \
  --header 'X-CSRF-Token: SeKSHJeFRNJtVIIHcy4Njb23dBatlh3IXQ_CSRHF6tk' \
  https://quip.bmi.stonybrook.edu/node/28134
*/