import React, { useState, useEffect } from "react"

function App() {
  const [data, setData] = useState({});
  useEffect(() => {
    fetch("/members")
    .then(
      (res) => {
        // console.log(res);
        res.json()
      }
    ).then(
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
    <>
      <div className="App">
        {JSON.stringify(data, null, 2)}
      </div>
    </>
  );
}

export default App;
