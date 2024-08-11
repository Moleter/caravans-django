const date = new Date();

const data = JSON.parse(document.getElementById("calendarData").textContent);

let startDate;
let endDate;

const checkReservation = (day) => {
  for (let index = 0; index < data.length; index++) {
    const element = data[index];
    {
      startDate = new Date(element.startDate);
      endDate = new Date(element.endDate);
      if (
        date.getFullYear() === startDate.getFullYear() ||
        date.getFullYear() === endDate.getFullYear()
      ) {
        if (
          date.getMonth() === startDate.getMonth() ||
          date.getMonth() === endDate.getMonth()
        ) {
          if (day >= startDate.getDate() && day <= endDate.getDate()) {
            return true;
          } else return false;
        } else return false;
      } else {
        return false;
      }
    }
  }
};

const renderCalendar = () => {
  date.setDate(1);

  const monthDays = document.querySelector(".days");

  const lastDay = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDate();

  const firstDayIndex = date.getDay();

  const prevLastDay = new Date(
    date.getFullYear(),
    date.getMonth(),
    0
  ).getDate();

  const lastDayIndex = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDay();

  const nextDays = 7 - lastDayIndex;

  const months = [
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

  document.querySelector(".date.h1").innerHTML = `${
    months[date.getMonth()]
  } ${date.getFullYear()}`;

  let days = "";

  let x;

  for (
    x = firstDayIndex - 1 >= 0 ? (x = firstDayIndex - 1) : (x = 6);
    x > 0;
    x--
  ) {
    days += `<div class="prev-date">${prevLastDay - x + 1}</div>`;
  }

  for (let i = 1; i <= lastDay; i++) {
    let isReservation = checkReservation(i);
    if (
      isReservation
      // i === new Date().getDate() &&
      // date.getMonth() === new Date().getMonth()
    ) {
      days += `<div class="today">${i}</div>`;
    } else {
      days += `<div>${i}</div>`;
    }
  }

  for (let j = 1; j <= nextDays; j++) {
    days += `<div class="next-date">${j}</div>`;
  }
  monthDays.innerHTML = days;
};

document.querySelector(".prev").addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
});

document.querySelector(".next").addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
});

renderCalendar();
