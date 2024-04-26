const backendURL = "http://localhost:8000";

export const healthCheck = async () => {
  const res = await fetch(backendURL + "/healthz", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  const resData = await res;

  if (resData.ok) {
    return resData.json();
  }
};

export const recipe = async (url: string) => {
  const urlParams = new URLSearchParams({ recipe_url: url });

  // Combine the base URL with the encoded parameters
  const fullUrl = `${backendURL}/recipe?${urlParams.toString()}`;
  const res = await fetch(fullUrl, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  const resData = await res;

  if (resData.ok) {
    const data = await resData.json();
    console.log("Data here");

    // if (data typeof Recipe)

    console.log(data);
    return data;

    // return resData.json();
  }
};
