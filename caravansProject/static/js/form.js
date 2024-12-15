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
  console.log(actualdate);
});
