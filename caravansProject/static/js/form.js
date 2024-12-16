const datastart = document.querySelector("#datastart");
const dataend = document.querySelector("#dataend");

let actualdate = new Date();
actualdate.setDate(actualdate.getDate() + 3);

datastart.setAttribute(
  "min",
  `${actualdate.getFullYear()}-${
    actualdate.getMonth() + 1
  }-${actualdate.getDate()}`
);

actualdate.setDate(actualdate.getDate() + 7);

dataend.setAttribute(
  "min",
  `${actualdate.getFullYear()}-${
    actualdate.getMonth() + 1
  }-${actualdate.getDate()}`
);

datastart.addEventListener("change", () => {
  actualdate = datastart.valueAsDate;
  actualdate.setDate(actualdate.getDate() + 7);

  console.log(actualdate.getDate() + " " + actualdate.getMonth());

  if (actualdate.getDate() < 10 && actualdate.getMonth() < 9) {
    dataend.setAttribute(
      "min",
      `${actualdate.getFullYear()}-0${
        actualdate.getMonth() + 1
      }-0${actualdate.getDate()}`
    );
  } else if (actualdate.getDate() < 10) {
    dataend.setAttribute(
      "min",
      `${actualdate.getFullYear()}-${
        actualdate.getMonth() + 1
      }-0${actualdate.getDate()}`
    );
  } else if (actualdate.getMonth() < 8) {
    dataend.setAttribute(
      "min",
      `${actualdate.getFullYear()}-0${
        actualdate.getMonth() + 1
      }-${actualdate.getDate()}`
    );
  } else {
    dataend.setAttribute(
      "min",
      `${actualdate.getFullYear()}-${
        actualdate.getMonth() + 1
      }-${actualdate.getDate()}`
    );
  }
});

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        let daysPicekd = document.querySelectorAll(".pickedDate");
        if (daysPicekd.length > 0) {
          let year =
            daysPicekd[0].parentElement.parentElement.childNodes[0]
              .childNodes[1].textContent;
          year = year.replace(/[^\d]/g, "");

          let month = parseInt(daysPicekd[0].getAttribute("data-month")) + 1;
          month < 10 ? (month = `0${month}`) : (month = `${month}`);

          day = daysPicekd[0].textContent;
          parseInt(day) < 10 ? (day = `0${day}`) : null;

          datastart.value = `${year}-${month}-${day}`;
        }
      }
    });
  },
  {
    root: null,
    threshold: 0.1,
  }
);

observer.observe(document.getElementById("contactForm"));
