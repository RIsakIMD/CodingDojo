
function ChangeName()
{
    document.querySelector(`.card-name`).innerHTML = `Anony Mouse`;
}

function RemoveRequest(name)
{
    document.querySelector(`#request-` + name).remove();
    document.querySelector(`.connection-header p`).innerHTML--;
}
