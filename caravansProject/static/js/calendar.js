const date = new Date();

const data = JSON.parse(document.getElementById("calendarData").textContent);

let startDate;
let endDate;

function caravanCheck() {
  let CaravanSelected = document.querySelector("#caravanSelect");

  return CaravanSelected.value;
}

const checkReservation = (day) => {
  for (let index = 0; index < data.length; index++) {
    const element = data[index];

    {
      startDate = new Date(element.startDate);
      endDate = new Date(element.endDate);

      if (caravanCheck() == element.caravan_id) {
        if (
          date.getFullYear() === startDate.getFullYear() ||
          date.getFullYear() === endDate.getFullYear()
        ) {
          if (
            date.getMonth() + 1 === startDate.getMonth() ||
            date.getMonth() + 1 === endDate.getMonth()
          ) {
            if (day >= startDate.getDate() && day <= endDate.getDate()) {
              return true;
            }
          }
        }
      }
    }
  }
  return false;
};

document.addEventListener("DOMContentLoaded", () => {
  const monthNames = [
    "Styczeń",
    "Luty",
    "Marzec",
    "Kwiecień",
    "Maj",
    "Czerwiec",
    "Lipiec",
    "Sierpień",
    "Wrzesień",
    "Październik",
    "Listopad",
    "Grudzień",
  ];

  const calendar = document.querySelector("#calendar");
  let currentDate = new Date();

  let firstClick = false;

  loadCalendar(currentDate);

  function loadCalendar(date) {
    calendar.innerHTML = "";
    addMonthToCalendar(date);
    addMonthToCalendar(new Date(date.getFullYear(), date.getMonth() + 1));
  }

  function addMonthToCalendar(date) {
    const monthElement = document.createElement("div");
    monthElement.classList.add("month");

    const monthNameElement = document.createElement("div");
    monthNameElement.classList.add("monthName");

    const monthNameSpan = document.createElement("span");

    const daysContainer = document.createElement("div");
    daysContainer.classList.add("days");

    monthElement.appendChild(monthNameElement);
    monthNameElement.appendChild(monthNameSpan);

    buildWeekdaysElement(monthElement);
    createButtons(monthNameElement);

    const year = date.getFullYear();
    const month = date.getMonth();
    monthNameSpan.textContent = `${monthNames[month]} ${year}`;

    daysContainer.innerHTML = "";

    const firstDay = new Date(year, month, 1).getDay();

    const daysInMonth = new Date(year, month + 1, 0).getDate();

    let i;
    firstDay == 0 ? (i = -6) : (i = 1);
    for (; i < firstDay; i++) {
      const emptyDiv = document.createElement("div");
      emptyDiv.classList.add("day-name");
      daysContainer.appendChild(emptyDiv);
    }

    for (let day = 1; day <= daysInMonth; day++) {
      const dayDiv = document.createElement("div");
      dayDiv.classList.add("day");

      dayDiv.setAttribute("data-month", date.getMonth());

      if (checkReservation(day)) {
        dayDiv.classList.remove("day");
        dayDiv.classList.add("reservation");
      }
      dayDiv.innerText = day;
      if (dayDiv.className === "day") {
        dayDiv.addEventListener("click", () => {
          dayDiv.classList.toggle("pickedDate");
          let pickedDays;
          let days = document.querySelectorAll(".day");

          if (!firstClick) {
            pickedDays = document.querySelectorAll(".pickedDate");
            days.forEach((day) => {
              if (
                pickedDays[0].getAttribute("data-month") ===
                pickedDays[1].getAttribute("data-month")
              ) {
                if (
                  parseInt(pickedDays[0].innerText) < parseInt(day.innerText) &&
                  parseInt(pickedDays[1].innerText) > parseInt(day.innerText) &&
                  pickedDays[0].getAttribute("data-month") ===
                  day.getAttribute("data-month")
                ) {
                  day.classList.toggle("pickedDate");
                }
              } else {
                if (
                  (pickedDays[0].getAttribute("data-month") ===
                    day.getAttribute("data-month") &&
                    parseInt(pickedDays[0].innerText) <
                    parseInt(day.innerText)) ||
                  (pickedDays[1].getAttribute("data-month") ===
                    day.getAttribute("data-month") &&
                    parseInt(pickedDays[1].innerText) > parseInt(day.innerText))
                ) {
                  day.classList.toggle("pickedDate");
                }
              }
            });
          } else {
            pickedDays = document.querySelectorAll(".pickedDate");
            pickedDays.forEach((day) => {
              day.classList.toggle("pickedDate");
            });
            pickedDays = null;
          }
          firstClick ? (firstClick = false) : (firstClick = true);

          //TODO: Error wkonsoli
        });
      }
      daysContainer.appendChild(dayDiv);
    }

    monthElement.appendChild(daysContainer);
    calendar.appendChild(monthElement);
  }

  function buildWeekdaysElement(ParentNode) {
    const dayNames = ["Pn", "Wt", "Śr", "Cz", "Pt", "Sb", "N"];

    const weekdeysDiv = document.createElement("div");
    weekdeysDiv.classList.add("weekdays");

    dayNames.forEach((dayName) => {
      let dayNameDiv = document.createElement("div");
      dayNameDiv.classList.add("day-name");

      dayNameDiv.innerText = dayName;
      weekdeysDiv.appendChild(dayNameDiv);
    });

    ParentNode.appendChild(weekdeysDiv);
  }

  function createButtons(monthNameElement) {
    const prevBtn = document.createElement("span");
    prevBtn.classList.add("prev");
    prevBtn.innerHTML = "&lt;";

    const nextBtn = document.createElement("span");
    nextBtn.classList.add("prev");
    nextBtn.innerHTML = "&gt;";

    monthNameElement.prepend(prevBtn);
    monthNameElement.appendChild(nextBtn);

    prevBtn.addEventListener("click", () => {
      currentDate.setMonth(currentDate.getMonth() - 1);
      loadCalendar(currentDate);
    });

    nextBtn.addEventListener("click", () => {
      currentDate.setMonth(currentDate.getMonth() + 1);
      loadCalendar(currentDate);
    });
  }
});
