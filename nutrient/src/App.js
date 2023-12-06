import React, { useState, useEffect } from "react"

function App() {
  const [data, setData] = useState("");
  useEffect(() => {
    fetch("/index_for_react")
    .then(
      (res) => {
        if (res.ok) {
          const rslt = res.json()
          console.log(rslt)
          return rslt
        } else {
          throw new Error("Bad response")
        }
      }
    )
    .then(
      js => {
        console.log(js);
        setData(js);
      }
    )
    .catch(
      (error) => {
        console.error("Error fetching data:", error)
      }
    );
  }, []);
  return (
    <div className="App">
      <ul>
        {data.nutrients.map(
          (item, index) => (<li key={index}>{item}</li>)
        )}
      </ul>
    </div>
  );
}

export default App;
