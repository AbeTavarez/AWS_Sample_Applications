exports.handler = async function(event, context) {
    event.Records.array.forEach(record => {
        const {body} = record
        console.log(body)
    });
    return {}
}