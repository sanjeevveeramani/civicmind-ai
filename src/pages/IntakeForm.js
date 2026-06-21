import { Form, Input, InputNumber, Select, Slider, Button, Card } from "antd";

function IntakeForm({ setResults, setPage }) {
  const [form] = Form.useForm();

  const handleSubmit = async (values) => {
    const mockData = {
      profile: values,

      scores: {
        path_a: {
          overall_score: 52.5,
          dimensions: [
            { dimension: "Infrastructure", score: 65 },
            { dimension: "Workforce", score: 40 },
            { dimension: "Data Maturity", score: 30 },
            { dimension: "Governance", score: 55 },
            { dimension: "Ethics", score: 45 },
            { dimension: "Public Trust", score: 60 },
          ],
        },

        path_b: {
          analysis:
            "This suburban community shows moderate readiness but governance maturity may be overstated.",
          recommendations: [
            "Launch data literacy program",
            "Create AI governance board",
          ],
          non_ai_alternatives: [
            "Manual data audit",
            "Community advisory committee",
          ],

          similar_cases: [
            {
              name: "Boulder, CO",
              outcome: "Success after 2 years",
              relevance: "Similar governance challenges",
            },
          ],
        },

        arbitrator: {
          status: "divergence",
          confidence: "needs_review",

          divergences: [
            {
              dimension: "Governance",
              path_a_score: 55,
              path_b_score: 32,
              difference: 23,
              explanation:
                "Policy exists on paper but similar communities struggled in practice.",
            },
          ],
        },
      },

      gaps: {
        percentiles: {
          Infrastructure: 70,
          Workforce: 45,
          Governance: 50,
          Ethics: 42,
          Trust: 60,
        },

        action_plan: {
          quick_wins: [
            "Publish AI policy",
            "Community workshops",
          ],

          medium_term: [
            "Staff AI training",
            "Data governance review",
          ],

          long_term: [
            "Create AI governance board",
            "Regional AI strategy",
          ],
        },
      },
    };

    setResults(mockData);
    setPage("results");
  };

  return (
    <Card title="Community Profile Assessment">
      <Form form={form} layout="vertical" onFinish={handleSubmit}>

        <Form.Item name="name" label="Community Name">
          <Input />
        </Form.Item>

        <Form.Item name="population" label="Population">
          <InputNumber style={{ width: "100%" }} />
        </Form.Item>

        <Form.Item name="community_type" label="Community Type">
          <Select
            options={[
              { value: "urban" },
              { value: "suburban" },
              { value: "rural" },
            ]}
          />
        </Form.Item>

        <Form.Item name="infrastructure" label="Infrastructure">
          <Slider min={0} max={100} />
        </Form.Item>

        <Form.Item name="workforce" label="Workforce Skills">
          <Slider min={0} max={100} />
        </Form.Item>

        <Form.Item name="data" label="Data Maturity">
          <Slider min={0} max={100} />
        </Form.Item>

        <Form.Item name="governance" label="Governance Readiness">
          <Slider min={0} max={100} />
        </Form.Item>

        <Form.Item name="ethics" label="Ethics & Policy">
          <Slider min={0} max={100} />
        </Form.Item>

        <Form.Item name="trust" label="Public Trust">
          <Slider min={0} max={100} />
        </Form.Item>

        <Form.Item name="context" label="Additional Context">
          <Input.TextArea rows={4} />
        </Form.Item>

        <Button type="primary" htmlType="submit">
          Analyze Community
        </Button>

      </Form>
    </Card>
  );
}

export default IntakeForm;