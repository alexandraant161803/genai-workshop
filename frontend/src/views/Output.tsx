import { Button } from "@netlight-design-system/nds-react";
import { OutputProps, Recipe } from "../types/types";

function Output({ data, onBack }: OutputProps) {
  console.log(data);

  if (!checkRecipeValidity(data)) 
   {
    return (
      <div>
        <h1 className="text-4xl font-bold">Almost there - please try again :) </h1>
        <div>{JSON.stringify(data)}</div>      
        <Button onClick={onBack}>Back</Button>
      </div>
    );
  }

  return (
    <>
      <h3 className="text-xl font-bold">SUCCESS</h3>
      <h1 className="text-4xl font-bold">{data?.name}</h1>
      <div className="flex flex-row justify-between w-full">
        <span>Portions: {data?.person_count}</span>
        <span>Total time: {data?.total_time_minutes}</span>
      </div>
      <div className="flex flex-col items-start w-full">
        <span className="font-bold ">Ingredients</span>
        <ul>
          {data?.ingredients.map((row) => {
            return (
              <li>
                {row.name}: {row.quantity} {row.unit}
              </li>
            );
          })}
        </ul>
      </div>
      <div className="flex flex-col items-start w-full">
        <span className="font-bold ">Steps</span>
        <ul>
          {data?.steps.map((row) => {
            return <li className="ml-4 list-disc">{row}</li>;
          })}
        </ul>
      </div>
      <Button onClick={onBack}>Back</Button>
    </>
  );
}
export default Output;

export function checkRecipeValidity(recipe: Recipe | undefined): boolean {
  if (!recipe) return false;
  const requiredFields: Array<keyof Recipe> = [
    "ingredients",
    "steps",
    "total_time_minutes",
    "person_count",
    "name"
  ];
  return requiredFields.every(field => recipe[field] !== null && recipe[field] !== undefined);
}