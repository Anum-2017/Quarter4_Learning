from agents import Agent, Runner, trace, InputGuardrailTripwireTriggered
from agents.guardrail import input_guardrail, GuardrailFunctionOutput
from agents.items import TResponseInputItem
from connection import config
from pydantic import BaseModel
from typing import Union
import asyncio
import rich


class TeacherResponse(BaseModel):
    reply: str
    isChangeRequest: bool


class ClassTimings(BaseModel):
    message: str


teacher_agent = Agent(
    name="Teacher Agent",
    instructions="""
    If the student attempts to change class timings, respond politely but firmly, 
    and set isChangeRequest = True; otherwise, set isChangeRequest = False.
    """,
    output_type=TeacherResponse
)


@input_guardrail
async def change_class_guardrail(ctx, agent: Agent, input: Union[str, list]):
    result = await Runner.run(teacher_agent, input, run_config=config, context=ctx)
    print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.isChangeRequest
    )

# Class Timings Agent with guardrail
class_timings_agent = Agent(
    name="ClassTiming_Agent",
    instructions="""
    You are a ClassTimings Agent. Your role is to ensure that students cannot change their class timings under any circumstances.
    """,
    input_guardrails=[change_class_guardrail],
)

async def main():
    with trace("Student_ClassTimings"):
        try:
            result = await Runner.run(class_timings_agent, "I want to change my class timings", run_config=config)
            rich.print(result)
            rich.print("[green]Guardrail did not trip[/green]")
        except InputGuardrailTripwireTriggered:
            rich.print("[red]Guardrail tripped: Class timings cannot be changed.[/red]")
   
if __name__ == "__main__":
    asyncio.run(main())



