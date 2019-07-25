const SPA_PAGES = [
    /^\/$/,
    /^\/search$/,
    /^\/libraries\/[^\/]+\/disks\/[^\/]+$/
];
const MAIN_PAGE = /\/index.html/;

exports.origin_request = (event, context, callback) => {

    const cf = event.Records[0].cf;
    const request = cf.request;
    const uri = request.uri;

    // Special case: refuse to serve index.html
    if(uri.match(MAIN_PAGE)) {
        callback(null, {
            body: '<html><head><title>404 Not Found</title></head><body><img src="https://http.cat/404" alt="404 Not Found"/></body></html>',
            bodyEncoding: 'text',
            headers: {
                'content-type': [{ value: 'text/html;charset=UTF-8' }]
            },
            status: '404',
            statusDescription: 'Not Found'
        })
    }

    // Check if URI matches any of the SPA_PAGES - if so, redirect CloudFront to fetch /index.html
    for(const r of SPA_PAGES) {
        if(uri.match(r)) {
           request.uri = "/index.html";
            callback(null, request);
        }
    }

    // Anything else can pass through
    callback(null, cf.request);
};
