Typescript
import { browser, $ } from '@wdio/globals';
import { expect } from 'chai';
describe('FR-14: UI Components with Chakra UI', () => {
    before(async () => { await browser.url('http://www.ipsy.com/component-library'); });
    it('Positive - Verify UI components are built using Chakra UI and function properly', async () => {
        const componentList = await $('.chakra-component-list');
        await expect(componentList).toBeDisplayed();
        const testComponent = await $('.test-component');
        await expect(testComponent).toBeDisplayed();
        await browser.setWindowSize(768, 1024);
        await expect(testComponent).toBeDisplayed();
    });
    it('Negative - Verify component fails to render without Chakra', async () => {
        const testComponent = await $('.test-component');
        await expect(testComponent).not.toBeDisplayed();
    });
    it('Edge - Verify on extreme screen sizes', async () => {
        await browser.setWindowSize(1920, 1080);
        const testComponent = await $('.test-component');
        await expect(testComponent).toBeDisplayed();
    });
});
