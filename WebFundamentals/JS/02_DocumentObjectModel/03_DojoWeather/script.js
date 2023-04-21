
function DisplayAlert()
{
    alert(`Loading weather report`);
}

function AcceptCookies()
{
    document.getElementById(`main-cookies`).remove();
}

function CtoF(temperature)
{
    return Math.round((temperature * 1.8) + 32);
}

function FtoC(temperature)
{
    return Math.round((temperature - 32) / 1.8);
}

function TemperatureChanged(element)
{
    let temperatures = document.querySelectorAll(".day-range p");
    
    temperatures.forEach(temperatures =>
    {
        temperatures.innerHTML = 
            element.value == `f` ? CtoF(temperatures.innerHTML) : FtoC(temperatures.innerHTML);
    });
}
